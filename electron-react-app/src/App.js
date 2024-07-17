import logo from './logo.svg';
import './App.css';
import MainPage from "./Pages/MainPage"
import { PageContainer } from './Resources/Themes/StyledComponents';
import Header from './Components/Header';

function App() {
  return (
    <div>
      <Header/>
      <MainPage/>
    </div>
  );
}

export default App;
