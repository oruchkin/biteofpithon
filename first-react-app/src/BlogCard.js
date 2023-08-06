
import { dumpLogs } from "./Utils";

const BlogCard = (props) => {
    // console.log(props);
    dumpLogs(props)
    return (
        <div className="BlogCard">
            <h3>{ props.title }</h3>
            <p>{ props.description }</p>
        </div>
    );
};

export default BlogCard;
