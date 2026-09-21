import assert from "node:assert/strict";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

import plugin from "../index.js";

const repository = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const skillsRoot = path.join(repository, "skills");

function registry(existing = new Map()) {
  return {
    entries: existing,
    ctx: {
      skill: {
        transform: async (callback) =>
          callback({
            get: (id) => existing.get(id),
            add: (skill) => existing.set(skill.id, skill),
          }),
      },
    },
  };
}

test("OpenCode v2 adapter registers each canonical skill with source content", async () => {
  const { entries, ctx } = registry();
  await plugin.setup(ctx);

  const names = (await readdir(skillsRoot, { withFileTypes: true }))
    .filter((entry) => entry.isDirectory() && entry.name.startsWith("gzs-"))
    .map((entry) => entry.name);
  assert.equal(plugin.id, "gz-skills");
  assert.deepEqual([...entries.keys()].sort(), names.sort());

  for (const id of names) {
    const skill = entries.get(id);
    const source = await readFile(skill.path, "utf8");
    assert.equal(path.dirname(skill.path), path.join(skillsRoot, id));
    assert.equal(skill.id, id);
    assert.ok(skill.name.startsWith("GovZero "));
    assert.ok(skill.description.length > 0);
    assert.ok(source.includes(skill.content));
    assert.ok(skill.content.startsWith("\n# GovZero "));
    assert.equal(skill.autoinvoke, !["gzs-git-sync", "gzs-session-handoff"].includes(id));
  }
});

test("OpenCode v2 adapter respects an existing project skill", async () => {
  const local = { id: "gzs-router", name: "Local Router" };
  const { entries, ctx } = registry(new Map([["gzs-router", local]]));
  await plugin.setup(ctx);
  assert.equal(entries.get("gzs-router"), local);
});
