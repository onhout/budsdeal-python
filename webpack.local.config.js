var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: __dirname,

    entry: {
        app: './src/index.js'
    }, // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

    output: {
        path: path.resolve('./static/'),
        publicPath: '/static/',
        chunkFilename: '[id]-[hash].chunk.js',
        filename: "[name]-[hash].js",
    },

    plugins: [
        // new webpack.optimize.UglifyJsPlugin(),
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            jQuery: 'jquery',             // bootstrap 3.x requires
        }),
        new ExtractTextPlugin('[name]-[hash].css')
    ],

    devtool: 'cheap-module-source-map',

    module: {
        loaders: [
            {test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
            {test: /\.less$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader!less-loader")}, //to transform less into CSS
            {test: /\.(jpe|jpg|png|woff|woff2|eot|ttf|svg)(\?.*$|$)/, loader: 'url-loader?limit=100000'},
            {test: /\.css$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader")},
            //changed the regex because of an issue of loading less-loader for font-awesome.
        ],
    },

    resolve: {
        modulesDirectories: ['node_modules', 'static/components'],
        extensions: ['', '.js', '.jsx']
    },
};