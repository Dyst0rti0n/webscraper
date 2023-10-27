
Next.js is a flexible react framework = fast web apps.

Building Blocks of web app
User Interface(UI) - How users will consume and interact with your app.
Routing - How user navigatee between different parts of your app
Data Fetching - Where your data lives and how to get it.
Rendering - When and where you render static or dynamic content
Integrations - What third-party services you use (CMS, auth, payments, etc) and how you connect to them.
Infrastructure - Where you deploy, store and run your app code(Serverless, CDN, Edge, etc)
Performance - How to optimise your application for end-users.
Scalability - How your app adapts as your team, data, traffic grow.
Dev Exp - Your team's experience building and maintaining you app

------What is react?
A JS library for building interactive UI, react provides helpful functions to build UI. 

-----What is Next.js?
Handles the tooling and configuration needed for React, and provides additional structure, features, and optimisations for your app.

Use React to build UI, then adopt Next.js to solve common app reqs

=====From Java to React====
----Rendering UI
When a user visits a web page, the server returns HTML file to the browser. Browser reads HTML then contructs Document Object Model (DOM)

----What is DOM?
An object rep of HTML elements. Acts as bridge between your code and UI and has a tree-like structure. (parent and child)
Use DOM methods and e.g JS to listen to user events and manipulate DOM by sel, add, upd, del specific elements in the UI. DOM can target specific elements and change their style and content.

====Updating the UI with JS and DOM methods====
Inside an ```index.html```,  give the div a unique id so you can target later. e.g ```id="app"``` . To write JS in HTML file add a 'script tag': ```<script type="text/javascript"></script>```  .Now inside the 'script' tag, you can use a DOM method, ```getElementById()``` , to select the '<div>' element by its 'id': ```const app = document.getElementById('app');```
	
----HTML vs DOM
DOM page is different from source code (orginal HTML file), HTML is the initial page content and DOM is updated page content from JS.

----Imperative vs Declarative programming
Imperative is like giving a chef a step-by-step guide to making a pizza and Declarative is like ordering a pizza. 

====Getting started with React====
react is the core React library
react-dom provides DOM-specific methods that enable use of React with the DOM

```#installing packages uses unpkg website
	<script src="https://unpkg.com/react@17/umd/react.development.js"></script>
	<script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>```
Instead of directly manipulating the DOM with plain JS, use ```ReactDOM.render()``` from 'react-dom' to tell React to render <h1> title.
```const app...
	ReactDOM.render(<h1>Develop. Preview. Ship. </h1>, app);```
Running this would result in syntax error because <h1>.....</h1> is not valid JS, it's JSX.

----What is JSX?
A syntax extension for JS that allows you to describe UI in a HTML-like syntax. You'll need JS compiler, such as Babel, to transform JSX into JS because browser's don't recognise this.

----Adding Babel to project
```<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>```
Also change scrip type to ```type=text/jsx``` to inform Babel what code to transform.
```<html>
		<body>
			<div ...></div>
			<script....react></script>
			<script....react-dom></script>
			<!-- Babel Script -->
			<script....babel></script>
			<script type="text/jsx">
				const app...
				ReactDOM....
			</script>
		</body>
	</html>

====Essential JS for React
learn JS first.
Core concepts of React to be familiar with:
-Components
-Props
-State

----Building UI with components
UIs broken down into smaller building blocks called components.
Components allow you to build self-contained, reusable snippets of code. Code is more maintainable, easy add, upd and del.

----Creating components
In React, components are functions. Inside your 'script' tag, write a function called 'header':
```<script type...>
		const app

		function header(){
		
		}

		ReactDOM....
	</script>```
A component is a function that returns UI elements. Inside the return statement of the function, you can write JSX:
``` function Header(){
		return (<h1>Develop. Preview. Ship. </h1>)
}
To render this component to the DOM, pass it as the first arg in ```ReactDOM.render()```
```ReactDOM.render(Header, app)```

#Components should be capitalised to distuingush between HTML and JS. Also using React com. same as HTML tags, with <>
```ReactDOM.render(<Header />, app)```

----Nesting components

Nest com. inside each other like regular HTML elements. 
Create a new comp.```HomePage```

```function Header(){
	return (<h1>Develop. Preview. Ship. </h1>);
}

function HomePage(){
	return <div></div>;
}

ReactDOM.render(<Header />, app);```

Then nest 'Header' comp. inside the new 'HomePage' comp:
```
function Header(){...}:

function HomePage(){
	return (
		<div>
			{/* Nesting the header comp. */}
			<Header />
		</div>
		);
}

ReactDOM.render(<Header />, app);
	```

====Displaying data with props
If you displayed '<header />' twice in HomePage, it would display it twice. But if you didn't knwo the information ahead of time, such as fetching or wanted to pass different text.

Regular HTML elements have attributes to pass info to change elements. e.g changing src of an <img> changes the img shown. Changing 'href' tag of an <a> tag changes destination of link. React uses props to pass these pieces of info.

----Using Props
HomePage comp. pass a 'title' prop to 'Header' just like HTML attributes:
```function HomePage(){
		return(
			<div>
				<Header title="React <3" />
			</div>
		);
}
```
And Header, the child comp, can accept these props as its first function parameter.
```function Header(props){
		console.log(props) // {title: "React <3>"};
		...
		}
console.log(props), you can see that it's an object with a title property.
Since 'props' is an object, you can use object destructuring to explicity name the values of props inside your function params:
```function Header({ title }) {
		console.log(title);
		return <h1>title</h1>;
}```

----Using Variables in JSX
To use variables defined, use '{}', JSX syntax that allows you to write regular JS directly in JSX markup.
``` // function Header({title}){
return <h1>{title}</h1>;
// }```
'{}' way to enter 'JS land' while in 'JSX land'. You can add any JS expression (something that evaluates to a single value) inside '{}'.
Examples:
1. An object property with dot notation
	```function Header (props) {
			return <h1>{props.title}</h1>;
		}```
2. A template literal
	```function Header({title}){
			return <h1>{'Cool ${title}'}</h1>;
		}
3. The returned value of a function
	```function createTitle(title) {
			if (title) {
				return title;
			} else {
			  return 'Default title';
			}
		 }

		function Header({title}){
			return <h1>{createTitle(title)}</h1>;
		}
4. Or ternary operators
	function Header({title}) {
		return <h1>{title ? title : 'Default Title'}</h1>;	
	}
So, changing 'index.html' to code below, comp. now accepts a generic title prop which can be reused.
```
function Header({ title }){
	return (
		<div>
			<Header />
		</div>
	);
}

function HomePage() {
	return (
		<div>
			<Header title="React <3">
			<Header title="A new title">
		</div>
	);
}
```

----Iterating through lists
You can use array methods to manipulate your data and generate UI elements that are identical in style but hold different pieces of information.
Add an array of names to your 'HomePage' comp
```
function HomePage(){
	const name = ['John Terry', 'Larry Crews', 'Robert Joy'];

	return (
		<div>
			<Header title="Develop. Preview. Ship. " />
			<ul>
				{names.map((name) => (
					<li>[name]</li>
				))}
			</ul>
		</div>
	);
}

Notice the use of '{}' to weave in and out of "JS" and "JSX" land.
Running this will return a missing 'key' prop. React needs something to uniquely id items in an array so it knows which elements to update in the DOM.
Recommened to use an item ID or something similar.
```
<ul>
	{names.map((name) => (
		<li key={name}>{name}</li>
	))}
</ul>

====Adding Interactivity with State
How React helps us add interactivity with state and event handlers.
Creating a like button inside your 'HomePage' comp. First, add a button element inside the return() statement:
```<button>Like</button>```

----Listening to Events
To make the button do something when clicked, you can make use of the 'onClick' event.
```function HomePage(){
		return (
			<div>
				<button onClick={}>Like</button>
			</div>	
		 );
	 }```
Event names are camelCased. The 'onClick' event is one of many possible events you can use to respond to user interaction. e.g you can use 'onChange' for input fields or 'onSubmit' for forms.

----Handling Events
Define a function to "handle" events whenever they are triggered. Create a function before the return statement called 'handleClick()':
```
function HomePage(){
	// ...

	function handleClick(){
		console.log("Increment like count")
	}

	return (
		<div>
			{/* ... */}
			<button onClick={}>Like</button>
		</div>	
	)

}```
Then you can call the 'handleClick' function when the 'onClick' event is triggered:
```<button onClick={handleClick}>Like</button>```

----Static and Hooks
React has a set of function called 'hooks'. Hooks allow you to add additional logic such as state to your comps. You can think of state as any info in your UI that changes over time, usually triggered by interaction.
You can use state to store and increment the no. of times a user has clicked the like button. This is what the React hook to manage state is called: 'useState()'
```function HomePage(){
		React.useState();
		}```
'useState()' returns an array, and you can access and use those array values inside your comp using array destructuring:
```
function HomePage(){
	const [] = React.useState();
	// ...
}```

This first item in the array is the state 'value', which you can name anything. It's recommended to name it to something descriptive
```
function HomePage(){
	const [likes] = React.useState();

	// ...
}```

The second item in the array is a function to 'update' the value. You can name the update function anything, but it's common to prefix it with 'set' followed by the name of the state variable you're updating: also inital value of likes to '0'
```
function HomePage(){
	const [likes, setLikes] = React.useState(0);
}```
Then you can check the initial state is working by using the state varible inside your comp.
```
function HomePage(){
	// ...
	const [likes, setLikes] = React.useState(0);

	return (
		// ...
		<button onClick={handleClick}>Like({likes})</button>
	);
}```
Finally you can add your state updater function, 'setLikes' in your 'HomePage' comp. Add it inside the 'handleClick()' function:
```
function HomePage(){
	// ...
	const ...

	function handleClick(){
		setLikes(likes + 1);
	}
	//...
}```
Clicking the button will now call the handleClick function, which calls the setLikes state updater function with a single arg of the current no. of likes + 1.

___Note___Unlike props which are passed to comps. as the first func para, the state is initiated and stored within a comp. You can pass the state info to children comps as props, but the logic for updating the state should be kept within the comp where state was initally created.

----Managing State
T
