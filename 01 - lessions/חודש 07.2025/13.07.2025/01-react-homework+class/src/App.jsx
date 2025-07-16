import { FavoriteColors } from './Componentes/FavoriteColors'
import { FilteredList } from './Componentes/FilteredList'
import { MovieRatings } from './Componentes/MovieRatings'
import { ProductList } from './Componentes/ProductList'
import { ProductListV2 } from './Componentes/ProductListV2'
import {StudentList} from './Componentes/StudentList'
import { TaskList } from './Componentes/TaskList'
import { Weather } from './Componentes/Weather'
import { ScoreList } from './Componentes/ScoreList'
import { OnlineUsers } from './Componentes/OnlineUsers'
import { ConditionalGreeting } from './Componentes/ConditionalGreeting'
function App() {

  return (
    <>
      <h1>Map</h1>
      <StudentList/>
      <ProductList/>
      <ProductListV2/>
      <TaskList/>
      <Weather/>
      <FilteredList/>
      <FavoriteColors/>
      <ScoreList/>
      <MovieRatings/>
      <OnlineUsers/>
      <ConditionalGreeting/>
    </>
  )
} 

export default App 
