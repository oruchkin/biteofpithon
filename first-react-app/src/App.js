import logo from './logo.svg';
import './App.css';
import JopaBlogCard from "./BlogCard";
import { isArrayEmpty } from "./Utils";
import { Component } from "react";

// function App() {
class App extends Component {
    state = {
        showBlogs: true,
        blogArr: [
            {
                id: 1,
                title: "Blog Title 1",
                description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum",
                likeCount: 10,
            },
            {
                id: 2,
                title: "Blog Title 2",
                description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum",
                likeCount: 0,
            },
            {
                id: 3,
                title: "Blog Title 3",
                description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum",
                likeCount: 0,
            },
        ]
    };

    blogObje = {
        title: "Blog Title 1",
        description: "Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum"
    };


    // test 2
    // const blogArr = null;

    onLikeBtnClick (pos) {
        const updatedBlogList = this.state.blogArr;
        const updatedBlogObj = updatedBlogList[pos]

        updatedBlogObj.likeCount = updatedBlogObj.likeCount + 1;
        updatedBlogList[pos] = updatedBlogObj
        this.setState({blogArr: updatedBlogList})

        console.log(updatedBlogObj)
    }



    onHideBtnClick = () => {
        // let updatedState = !this.state.showBlogs
        // this.setState({showBlogs: updatedState });
        this.setState((prevState, prevProps) => {
            return { showBlogs: !prevState.showBlogs };
        });

        console.log(this.showBlogs);
    };

    // test

    render() {

        const blogCards = isArrayEmpty(this.state.blogArr) ? [] : this.state.blogArr.map((item, pos) => {
            return (
                <JopaBlogCard className="blog"
                              title={ item.title }
                              likeCount={ item.likeCount }
                              description={ item.description }
                              onLikeBtnClick={() => this.onLikeBtnClick(pos)}
                              key={ pos }/>
            );
        });

        console.log('Render Called');
        console.log(this.state);
        return (
            <div className="App">
                <button onClick={ this.onHideBtnClick }>{ this.state.showBlogs ? 'Hide list' : 'Show list' }</button>
                <br/>
                { this.state.showBlogs ? blogCards : null }
            </div>
        );
    }
}

export default App;
