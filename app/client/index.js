import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, IndexRoute, NotFoundRoute, Link, browserHistory } from 'react-router';
import { RepoCard, RepoCardList } from './components/RepoCardComponents'
import { AccCard, AccCardList } from './components/AccCardComponents'

class About extends Component {

  constructor(props) {
    super(props)
    this.state = {}
  }

  componentWillMount() {
    this.props.navUpdate("About")
  }

  render() {
    return (
      <div className="container">
        <AccCardList />
      </div>
    )
  }

}

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {}
  }

  componentWillMount() {
    this.props.navUpdate("Home")
  }

  render() {
    return (
      <div className="container">
        <RepoCardList />
      </div>
    )
  }

}

class NoMatch extends Component {

  constructor(props) {
    super(props)
    this.state = {}
  }

  componentWillMount() {
    this.props.navUpdate("404")
  }

  render() {
    return (
      <p>Invalid scope! Go back to</p>
    )
  }

}

class Wrapper extends Component {

  constructor(props) {
    super(props)
    this.state = {
      "nav": {
        "Home": true,
        "About": false,
        "404": false
      }
    }
    this.changeRoute = this.changeRoute.bind(this)

  }

  changeRoute(newRoute) {
    console.log(newRoute)
    let home = newRoute === "Home" ? true : false
    let about = newRoute === "About" ? true : false
    let notFound = newRoute === "404" ? true : false
    this.setState({
      "nav": {
        "Home": home,
        "About": about,
        "404": notFound
      }
    })
  }

  render() {
    console.log("Main rendered")
    return (
      <div>
        <div className="main-nav">
          <ul>
            <li className={ this.state.nav["Home"] ? `active` : `off` }><Link to={`/`}>Home</Link></li>
            <li className={ this.state.nav["About"] ? `active` : `off` }><Link to={`/about`}>Collabs</Link></li>
            <li className={ this.state.nav["404"] ? `active` : `off` }><Link to={`/not`}>404</Link></li>
          </ul>
        </div>
        { React.cloneElement(this.props.children, { navUpdate: this.changeRoute }) }
      </div>
    )
  }

}

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path="/" component={Wrapper}>
      <IndexRoute component={App}/>
      <Route path="/about" component={About}/>
      <Route path="*" component={NoMatch}/>
    </Route>
  </Router>
), document.getElementById("mainNode"))
