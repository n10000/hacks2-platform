import { getCollection } from "astro:content";

export const prerender = true;

const SITE = "https://hacks2.com";

const staticPaths = [
  "/",
  "/ai-workflow-templates/",
  "/business-operations-pack/",
  "/chatgpt-vs-claude/",
  "/disclosure/",
  "/notes/",
  "/refund-policy/",
  "/roi-calculator/",
  "/starter-pack/",
  "/tools/",
  "/workflows/",
];

function escapeXml(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");
}

function isoDate(value: Date) {
  return value.toISOString().slice(0, 10);
}

type SitemapEntry = {
  loc: string;
  lastmod?: string;
};

export async function GET() {
  const [workflows, notes, tools] = await Promise.all([
    getCollection("workflows"),
    getCollection("notes"),
    getCollection("tools"),
  ]);

  const entries: SitemapEntry[] = [
    ...staticPaths.map((path) => ({ loc: new URL(path, SITE).toString() })),
    ...workflows.map((workflow) => ({
      loc: new URL(`/workflows/${workflow.id}/`, SITE).toString(),
      lastmod: isoDate(workflow.data.updatedAt ?? workflow.data.publishedAt),
    })),
    ...notes.map((note) => ({
      loc: new URL(`/notes/${note.id}/`, SITE).toString(),
      lastmod: isoDate(note.data.updatedAt ?? note.data.publishedAt),
    })),
    ...tools.map((tool) => ({
      loc: new URL(`/tools/${tool.id}/`, SITE).toString(),
    })),
  ];

  const deduped = Array.from(
    new Map(entries.map((entry) => [entry.loc, entry])).values(),
  ).sort((a, b) => a.loc.localeCompare(b.loc));

  const body = deduped
    .map((entry) => {
      const lastmod = entry.lastmod
        ? `\n    <lastmod>${escapeXml(entry.lastmod)}</lastmod>`
        : "";
      return `  <url>\n    <loc>${escapeXml(entry.loc)}</loc>${lastmod}\n  </url>`;
    })
    .join("\n");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>\n`;

  return new Response(xml, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
