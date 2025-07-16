export function Student(props) {
    return (
        <>
            <p>
                {props.Fname} {props.Lname} - 
                {props.Grade > 65 ? 
                    <span style={{ color: "green" }}>{props.Grade}</span> : 
                    <span style={{ color: "red" }}>{props.Grade}</span>
                }
            </p>
        </>
    );
}