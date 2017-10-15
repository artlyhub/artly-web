var debug = process.env.NODE_ENV !== 'production'
var path = require('path')
var webpack = require('webpack')

module.exports = {
  // define entry point
  entry: {
    'index-bundle': ['babel-polyfill', './static-dev/js/Index.js'],
  },

  // define output point
  output: {
    path: path.join(__dirname, 'static-dev/dist'),
    filename: '[name].js'
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          cacheDirectory: true,
          presets: ['react', 'es2015', 'stage-0'],
          plugins: ['react-html-attrs', 'transform-class-properties', 'transform-decorators-legacy']
        }
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
        // loader: "style-loader!css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]"
      },
      {
        test: /\.scss$/,
        loader: 'style-loader!css-loader!sass-loader'
      },
      {
        test: /\.(png|jpg|gif|svg|eot|ttf|woff|woff2)$/,
        loader: 'url-loader?limit=100000'
      }
    ]
  },

  plugins: debug ? [] : [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({ minimize: true,
                                          mangle: false,
                                          sourcemap: false }),
  ]
}
