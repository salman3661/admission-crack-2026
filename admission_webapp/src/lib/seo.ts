import { useEffect } from 'react';

export interface SEOConfig {
  title: string;
  description: string;
  path: string;
  jsonLd?: Record<string, unknown>;
}

const SITE_URL = 'https://admissionwebapp.vercel.app';
const OG_IMAGE = `${SITE_URL}/logo512.png`;

function upsertMeta(attr: 'name' | 'property', key: string, content: string) {
  let el = document.querySelector(`meta[${attr}="${key}"]`) as HTMLMetaElement | null;
  if (!el) {
    el = document.createElement('meta');
    el.setAttribute(attr, key);
    document.head.appendChild(el);
  }
  el.setAttribute('content', content);
}

function upsertLink(rel: string, href: string) {
  let el = document.querySelector(`link[rel="${rel}"]`) as HTMLLinkElement | null;
  if (!el) {
    el = document.createElement('link');
    el.setAttribute('rel', rel);
    document.head.appendChild(el);
  }
  el.setAttribute('href', href);
}

export function useSEO({ title, description, path, jsonLd }: SEOConfig) {
  useEffect(() => {
    const cleanPath = path.startsWith('/') ? path : `/${path}`;
    const canonical = `${SITE_URL}${cleanPath === '/' ? '' : cleanPath}`;

    document.title = title;
    upsertMeta('name', 'description', description);
    upsertLink('canonical', canonical);

    upsertMeta('property', 'og:type', 'website');
    upsertMeta('property', 'og:title', title);
    upsertMeta('property', 'og:description', description);
    upsertMeta('property', 'og:url', canonical);
    upsertMeta('property', 'og:image', OG_IMAGE);

    upsertMeta('name', 'twitter:card', 'summary_large_image');
    upsertMeta('name', 'twitter:title', title);
    upsertMeta('name', 'twitter:description', description);
    upsertMeta('name', 'twitter:image', OG_IMAGE);

    const ldPayload = {
      '@context': 'https://schema.org',
      '@graph': [
        {
          '@type': 'Organization',
          name: 'Admission Crack 2026',
          url: SITE_URL,
          logo: OG_IMAGE,
        },
        {
          '@type': 'SoftwareApplication',
          name: 'Admission Crack 2026 — DU Ka & MAT Prep Engine',
          applicationCategory: 'EducationalApplication',
          operatingSystem: 'Web, Android, iOS',
          url: canonical,
        },
        {
          '@type': 'BreadcrumbList',
          itemListElement: [
            { '@type': 'ListItem', position: 1, name: 'Home', item: SITE_URL },
            ...(cleanPath !== '/'
              ? [{ '@type': 'ListItem', position: 2, name: title, item: canonical }]
              : []),
          ],
        },
        ...(jsonLd ? [jsonLd] : []),
      ],
    };

    let script = document.getElementById('ac-jsonld') as HTMLScriptElement | null;
    if (!script) {
      script = document.createElement('script');
      script.id = 'ac-jsonld';
      script.type = 'application/ld+json';
      document.head.appendChild(script);
    }
    script.textContent = JSON.stringify(ldPayload);
  }, [title, description, path, jsonLd]);
}
