import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');

  return (
    <div>
      <input 
        type="text" 
        value={text} 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Type here..."
      />
      <h1>{text}</h1>
    </div>
  );
}

export default App;
