import path from "node:path";
import { fileURLToPath } from "node:url";

const pluginDirectory = path.dirname(fileURLToPath(import.meta.url));
const skillsPath = path.resolve(pluginDirectory, "../../skills");

const GzSkillsPlugin = async () => ({
  config: async (config) => {
    config.skills ??= {};
    config.skills.paths ??= [];

    if (!config.skills.paths.includes(skillsPath)) {
      config.skills.paths.push(skillsPath);
    }
  },
});

export { GzSkillsPlugin };
export default GzSkillsPlugin;
