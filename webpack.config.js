module.exports = {
  // define entry point
  entry: "./static-dev/js/src/script-1.js",

  // define output point
  output: {
    path: __dirname + "/static-dev/js/dist",
    filename: "bundle.js"
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: "babel-loader",
        query: {
          presets: ["es2015"]
        }
      },
      {
        test: /\.scss$/,
        loader: "style-loader!css-loader!sass-loader"
      }
    ]
  }
}
