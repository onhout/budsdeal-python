var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: __dirname,

    entry: {
        app: './client/index.js'
    }, // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

    output: {
        path: path.resolve('/static/'),
        publicPath: '/static/',
        chunkFilename: '[id]-[hash].chunk.js',
        filename: "[name]-[hash].js",
    },

    plugins: [
        // new webpack.optimize.UglifyJsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            jQuery: 'jquery',             // bootstrap 3.x requires
        })
    ],

    devtool: 'source-map',

    module: {
        loaders: [
            {test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
            {test: /\.less$/, loader: "style!css!autoprefixer!less"} //to transform less into CSS
        ],
    },

    resolve: {
        modulesDirectories: ['node_modules', 'static/components'],
        extensions: ['', '.js', '.jsx']
    },
};