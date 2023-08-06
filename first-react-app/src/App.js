import logo from './logo.svg';
import './App.css';
import BlogCard from "./BlogCard";

function App() {
    const blogObje = {
        title: "Blog Title 1",
        description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    };

    const blogArr = [
        {
            id: 1,
            title: "Blog Title 1",
            description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
        },
        {
            id: 2,
            title: "Blog Title 2",
            description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
        },
        {
            id: 3,
            title: "Blog Title 3",
            description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
        },
    ];

    const blogCards = blogArr.map((item, pos) => {
        // console.log(item);
        return (
            <BlogCard className="blog" title={ item.title } description={ item.description } key={ pos }/>
            //
            // <div className="BlogCard" key={item.id}>
            //     <h3>{ item.title }</h3>
            //     <p>{ item.description }</p>
            //     <p>{ item.id }</p>
            // </div>
        );
    });

    return (
        <div className="App">
            { blogCards }


        </div>
    );
}

export default App;
