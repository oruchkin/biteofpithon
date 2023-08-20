import { dumpLogs } from "./Utils";
// import './BlogCard.css';
import classes from './BlogCardM.module.css'

const BlogCard = (props) => {
    // console.log(props);
    dumpLogs(props);
    return (
        // <div className="BlogCard">
        <div className={ classes.NewBlogCard }>
            <h3>{ props.title }</h3>
            <p>{ props.description }</p>
        </div>
    );
};

export default BlogCard;
