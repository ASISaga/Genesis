/.github/agents should comply to the following - Agent profiles are Markdown files with YAML frontmatter. In their simplest form, they include:

Name: A unique identifier for the custom agent.
Description: Explains the agent's purpose and capabilities.
Prompt: Custom instructions that define the agent's behavior and expertise.
Tools (optional): Specific tools the agent can access. By default, agents can access all available tools, including built-in tools and MCP server tools. 