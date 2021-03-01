const webpack = require('webpack')

module.exports = {
    lintOnSave: true,
    configureWebpack: {
        devServer: {
            historyApiFallback: true
        },
        plugins: [
            new webpack.LoaderOptionsPlugin({
                test: /\.scss$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader'
                ]
            })
        ]
    },
}
