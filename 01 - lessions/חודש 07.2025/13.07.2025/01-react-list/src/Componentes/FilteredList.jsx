export function FilteredList() {
    const products = [
        { name: 'ינבר', inStock: true },
        { name: 'מקדחת', inStock: false },
        { name: 'יסד', inStock: true },
        { name: 'חדפסח', inStock: false },
        { name: 'יטען', inStock: true },
    ];

    let filterMapInstock = products
        .filter((product) => product.inStock)//אחרי הפילטר 
        .map((item, index) => { //עושה עליו מאפ
            return (
                <li key={index}>{item.name}</li>
            );
        });

    return (
        <div>
            <h1>Exe 5 - Filter list</h1>
            <ul>
                {filterMapInstock}
            </ul>
        </div>
    );
}