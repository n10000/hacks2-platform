import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const workflows = defineCollection({
  loader: glob({ base: "./src/content/workflows", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    category: z.string(),
    readTime: z.string(),
    featured: z.boolean().default(false),
    outcomes: z.array(z.string()),
    tools: z.array(z.string()),
  }),
});

const tools = defineCollection({
  loader: glob({ base: "./src/content/tools", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    pricing: z.string(),
    website: z.string().url(),
    verdict: z.string(),
    featured: z.boolean().default(false),
  }),
});

const notes = defineCollection({
  loader: glob({ base: "./src/content/notes", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    category: z.string(),
    readTime: z.string(),
  }),
});

export const collections = { workflows, tools, notes };
