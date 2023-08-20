import { dumpLogs } from "./Utils";
// import './BlogCard.css';
import classes from './BlogCardM.module.css';
import { Component } from "react";

class BlogCard extends Component {
    state = {
        likeCount: 0
    };

    onLikeBtnClick = () => {
        this.setState((prevState, prevProp) => {
            return { likeCount: prevState.likeCount + 1 };
        });
    }

    render() {
        dumpLogs(this.props);
        return (
            <div className={ classes.NewBlogCard }>
                <h3>{ this.props.title }</h3>
                <p>{ this.props.description }</p>
                <p>Like Count: <span className={ classes.LikeCount }>{ this.state.likeCount }</span></p>
                <button onClick={ this.onLikeBtnClick }>Like</button>
            </div>
        );
    }
};

export default BlogCard;
