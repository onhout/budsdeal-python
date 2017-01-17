var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,

    entry: {
        app: './client/index.js'
    }, // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

    output: {
        path: path.resolve('./static/dist/'),
        chunkFilename: '[id]-[hash].chunk.js',
        filename: "[name]-[hash].js",
    },

    plugins: [
        // new webpack.optimize.UglifyJsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'}),
    ],

    module: {
        loaders: [
            {test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
        ],
    },

    resolve: {
        modulesDirectories: ['node_modules', 'static/components'],
        extensions: ['', '.js', '.jsx']
    },
};