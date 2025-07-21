import { useState } from 'react'
import Counter from './Components/counter'
import Clock from './Components/counter'
import { Stopper } from './Components/stopper'
import { Quote } from './Components/Quote'

function App() {


  return (
    <>
    <Clock/>
    <Counter/>
    <Stopper/>
    <Quote/>
    </>
  )
}

export default App
