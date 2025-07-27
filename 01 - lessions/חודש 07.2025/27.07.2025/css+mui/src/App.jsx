import { Counter } from "./Components/Counter"
import {TextField} from '@mui/material';
import * as React from 'react';
import Switch from '@mui/material/Switch';

function App() {

    const label = { inputProps: { 'aria-label': 'Switch demo' } };
  return (
    <>
    <h1>counter</h1>
    <Counter/>
      <h1>mui</h1>
      <p>כל זה לקוח מהאתר שיש את הלינק אליו כאן </p>
      <a href="https://mui.com/material-ui/react-switch/" target="_blank">click for the website</a>
      <br /><br />
      <TextField id="outlined-basic" label="Outlined" variant="outlined" />
      <TextField id="filled-basic" label="Filled" variant="filled" />
      <TextField id="standard-basic" label="Standard" variant="standard" /> 
      <div>
      <Switch {...label} defaultChecked />
    </div>
    
    </>
  )
}

export default App
