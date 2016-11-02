var webpack = require("webpack");

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
    )
  ]
}
