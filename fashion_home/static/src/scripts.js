document.addEventListener("DOMContentLoaded", ()=>{
// adds a time to the page
ReactDOM.render(<Clock/>, document.getElementById("time"));



});


class Clock extends React.Component{
	constructor(props){
		super(props);
		this.state={date: new Date()}
	}
	componentDidMount(){
		this.timeId=setInterval(()=>this.tick(),1000);
	}
	componentWillUnmount(){
		clearInterval(this.timeId);
	}

	tick(){
		this.setState({date:new Date()});
	}
	render(){
		return <span> {this.state.date.toLocaleTimeString()} </span>
	}
}