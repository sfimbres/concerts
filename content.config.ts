import { defineContentConfig, defineCollection } from '@nuxt/content'
import { z } from 'zod'

export default defineContentConfig({
  collections: {
    concerts: defineCollection({
      type: 'data',
      source: 'concerts/*.json',
      schema: z.object({
        artists: z.array(z.string()),
        headliner: z.string(),
        tour: z.string(),
        festival: z.string(),
        venue: z.string(),
        location: z.string(),
        date_from: z.string(),
        date_to: z.string(),
        cid: z.string()
      })
    })
  }
})