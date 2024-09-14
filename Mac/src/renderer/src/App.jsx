import React from 'react';
 // Import your CSS file for styling
 import './App.css';
import Versions from './components/Versions'; // Assuming Versions component displays app versions
import electronLogo from './assets/electron.svg';

function App() {
  const ipcHandle = () => window.electron.ipcRenderer.send('ping'); // Function to send IPC message

  return (
    <div className="App"> {/* Wrap entire content in a styled container */}
      <header className="header"> {/* Create a header section */}
        <img alt="Electron Logo" className="logo" src={electronLogo} />
        <h1 className="title">Let's Learn & Play!</h1> {/* Replace "Build an Electron app..." */}
      </header>
      <main className="main-content"> {/* Main content area */}
        <p className="intro">
          Welcome to your exciting learning adventure! Here, we'll explore the
          wonderful world of knowledge and have fun along the way.
        </p>
        <section className="learning-areas"> {/* Section for different learning areas */}
          <h2>Let's explore these amazing subjects:</h2>
          <ul className="subjects"> {/* Unordered list for subjects */}
            <li>Numbers & Counting</li>
            <li>Animals & Colors</li>
            <li>Shapes & Sizes</li>
            <li>The Alphabet & Letters</li>
            <li>Add your own learning areas here!</li>
          </ul>
        </section>
        <section className="activities"> {/* Section for interactive activities */}
          <h2>Fun activities to keep you engaged:</h2>
          <ul className="activity-list"> {/* Unordered list for activities */}
            <li>Play interactive games based on learning areas.</li>
            <li>Color and draw pictures to express your creativity.</li>
            <li>Sing along to educational songs and rhymes.</li>
            <li>Watch short animated videos to learn new things.</li>
            <li>Add your own engaging activities here!</li>
          </ul>
        </section>
      </main>
      <footer className="footer"> {/* Footer section */}
        <div className="actions">
          <div className="action">
            <a
              href="https://electron-vite.org/"
              target="_blank"
              rel="noreferrer"
            >
              Documentation
            </a>
          </div>
          <div className="action">
            <a target="_blank" rel="noreferrer" onClick={ipcHandle}>
              Send IPC
            </a>
          </div>
        </div>
        <p className="copyright">Built with Electron & React</p>
        <Versions /> {/* Display app versions in the footer */}
      </footer>
    </div>
  );
}

export default App;