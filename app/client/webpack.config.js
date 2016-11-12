var webpack = require("webpack");
var CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  entry: "./index.js",
  output: {
    path: "../static/js",
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: 'babel',
        query: {
          presets: ['es2015','react']
        }
      }
    ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin(
    	{
    		minimize: true,
    		compress: false
    	}
    ),
    new CompressionPlugin({
      asset: "[path].gz[query]",
      algorithm: "gzip",
      test: /\.js$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ]
}
