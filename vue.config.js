const path = require('path');

module.exports = {
    publicPath: '/rokaf-pictogram-web/',
    outputDir: 'docs',
    configureWebpack: {
        resolve: {
            alias: {
                '@': path.join(__dirname, 'src/')
            }
        }
    }
}