import React, { Component } from 'react'
import ReactDOM from 'react-dom'

import '../../css/src/test.css'


class App extends Component {
  render() {
    return (
      <div class="intro-component">
          <h1>Let's see if this works...</h1>
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('root'))
