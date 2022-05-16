const path = require('path')

//const pathPrefix = process.env.KB_BASE_PATH || '/'
const pathPrefix = process.env.KB_BASE_PATH || 'gatsby-project-kb'

module.exports = {
  pathPrefix,
  siteMetadata: {
    title: `Second Brain`,
    description: `Your personal knowledge base`,
    author: `@hikerpig`,
  },
  plugins: [
    {
      resolve: 'gatsby-theme-kb',
      options: {
        contentPath: path.resolve(__dirname, 'content'),
        wikiLinkLabelTemplate: '[[{{ title }}]]',
        getPluginMdx(defaultPluginMdx) {
          defaultPluginMdx.options.gatsbyRemarkPlugins.push({
            resolve: 'gatsby-remark-prismjs',
            options: {
              noInlineHighlight: true,
            },
          })
          return defaultPluginMdx
        },
      },
    },
    'gatsby-plugin-no-sourcemaps',
  ],
}
