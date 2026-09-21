import { readFile, readdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const pluginDirectory = path.dirname(fileURLToPath(import.meta.url));
const skillsPath = path.resolve(pluginDirectory, "../../skills");
const explicitOnly = new Set(["gzs-git-sync", "gzs-session-handoff"]);

function skillFromFile(id, location, source) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/.exec(source);
  if (!match) throw new Error(`Invalid skill frontmatter: ${location}`);

  const field = (key) => {
    const value = new RegExp(`^${key}:\\s*(.+)$`, "m").exec(match[1])?.[1]?.trim();
    if (!value) throw new Error(`Missing ${key} in ${location}`);
    return value;
  };

  if (field("name") !== id) {
    throw new Error(`Skill name does not match directory: ${location}`);
  }

  const title = /^# (.+)$/m.exec(match[2])?.[1];
  if (!title) throw new Error(`Missing skill title: ${location}`);

  return {
    id,
    name: title,
    description: field("description"),
    path: location,
    content: match[2],
    autoinvoke: !explicitOnly.has(id),
  };
}

async function bundledSkills() {
  const entries = await readdir(skillsPath, { withFileTypes: true });
  return Promise.all(
    entries
      .filter((entry) => entry.isDirectory() && entry.name.startsWith("gzs-"))
      .map(async (entry) => {
        const location = path.join(skillsPath, entry.name, "SKILL.md");
        return skillFromFile(entry.name, location, await readFile(location, "utf8"));
      }),
  );
}

// OpenCode v2 discovers package plugins through their default export.
export default {
  id: "gz-skills",
  async setup(ctx) {
    const skills = await bundledSkills();
    await ctx.skill.transform((editor) => {
      for (const skill of skills) {
        if (!editor.get(skill.id)) editor.add(skill);
      }
    });
  },
};
