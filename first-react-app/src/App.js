import logo from './logo.svg';
import './App.css';
import Jopa from "./BlogCard";
import { isArrayEmpty } from "./Utils";

function App() {
    const blogObje = {
        title: "Blog Title 1",
        description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    };

    // const blogArr = [
    //     {
    //         id: 1,
    //         title: "Blog Title 1",
    //         description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    //     },
    //     {
    //         id: 2,
    //         title: "Blog Title 2",
    //         description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    //     },
    //     {
    //         id: 3,
    //         title: "Blog Title 3",
    //         description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    //     },
    // ];

    const blogArr = null;

    const blogCards = isArrayEmpty(blogArr) ? [] : blogArr.map((item, pos) => {
        return (
            <Jopa className="blog" title={ item.title } description={ item.description } key={ pos }/>
        );
    });

    return (
        <div className="App">
            { blogCards }


        </div>
    );
}

export default App;
