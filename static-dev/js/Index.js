import React, { Component } from 'react'
import ReactDOM from 'react-dom'

import Navbar from './components/Navbar'

import 'semantic-ui-css/semantic.min.css'
import '../css/Index.css'


class Index extends Component {
  render() {
    return (
      <div>
        <Navbar />
      </div>
    )
  }
}

ReactDOM.render(<Index />, document.getElementById('root'))
