import logo from './logo.svg';
import './App.css';

function App() {
    const firstName = 'Oleg';
    const lastName = "Ruchkin";
    const age = 31;
    const job = "Developer";
    const inputPlaceHolder = 'Enter Your Details const';

    const detailsInputBox = <input placeholder={ inputPlaceHolder } autoComplete/>;

    const mArr = [1, 2, 3, 4];

    const mObj = {
        name: 'Toto',
        age: 55,
    }

    const getFullName = () => {
        return `${ firstName } ${ lastName }`;
    };

    return (
        <div className="App">
            {/*<h3>Full Name: { `${ firstName } ${ lastName }` }</h3>*/ }
            <h3>Full Name: { getFullName() }</h3>
            <p>Age: { mObj.age } </p>
            <p>Job: { job }</p>
            {/*<input placeholder={ inputPlaceHolder } type="text"/>*/ }
            { detailsInputBox }
            <br/>
            { mArr[0] }
            {mObj.name}
        </div>
    );
}

export default App;
