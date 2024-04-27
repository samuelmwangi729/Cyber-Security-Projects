import React, { Component } from 'react'
import img1 from './assets/1.png'
import img2 from './assets/2.jpg'
import img3 from './assets/3.jpg'
import img4 from './assets/4.jpg'
import img5 from './assets/5.jpg'
import img6 from './assets/6.jpg'
import img7 from './assets/7.jpg'
import img8 from './assets/8.jpg'
import img9 from './assets/9.jpg'
class App extends Component {
  constructor() {
    super()
    this.shuffleImages = this.shuffleImages.bind(this)
  }
  state = {
    images: {
      'computer': img1,
      'trailer': img2,
      'houser': img3,
      'car': img4,
      'plane': img5,
      'dog': img6,
      'cat': img7,
      'bird': img8,
      'baby': img9
    }
  }
  shuffleObject(obj) {
    const entries = Object.entries(obj);
    for (let i = entries.length - 1; i > 0; i--) {
      const j =
        Math.floor(Math.random() * (i + 1));
      [entries[i], entries[j]] =
        [entries[j], entries[i]];
    }
    return Object.fromEntries(entries);
  }
  shuffleImages = () => {
    const newImages = this.shuffleObject(this.state.images)
    this.setState({
      images: newImages
    })
    for (let [key, value] of Object.entries(newImages)) {
      console.log(key, value);
    }

  }
  render = () => {
    return (
      <>
        <section className='w-[60%] h-screen m-auto font-serif text-xl flex flex-col justify-center items-center'>
          <h1 className='text-center font-serif text-3xl mt-2'>Graphical Authentication</h1>
          <div className="w-full">
            <form action="" className='w-[70%] m-auto text-sm shadow-xl p-2 bg-gray-200 flex flex-col gap-2 items-start' onSubmit={(e) => e.preventDefault}>
              <div className="form-group p-2">
                <label htmlFor="" className="label-control">Username</label>
                <input type="text" name="" id="" className="form-control p-2" />
              </div>
              <div className="graphical-password">
                <label htmlFor="" className="label-control">
                  Graphical Password
                </label>
                <div className="w-full">
                  <div className="flex flex-row justify-between items-center">
                    <div className="w-[50%] grid grid-cols-3">
                      {Object.keys(this.state.images).map((image,index)=>(
                        index<=2 ? (
                          <div className="object-fit w-[90px] h-[60px]" key={index}>
                            <img src={this.state.images[image]} alt="" /> 
                          </div>
                        ):null
                      ))}
                    </div>
                    <div className="w-[50%] grid grid-cols-3 gap-3">
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 1</label>
                        <input type="text" className='w-20' />
                      </div>
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 2</label>
                        <input type="text" className='w-20' />
                      </div>
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 3</label>
                        <input type="text" className='w-20' />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="flex flex-row justify-between items-center w-full gap-3">
                <button className='p-2 bg-orange-500 text-white text-bold w-[50%]' type='button' onClick={this.shuffleImages}>
                  Shufle Images
                </button>
                <button className=' w-[50%] p-2 bg-orange-500 text-white text-bold'>
                  Submit
                </button>
              </div>
            </form>
          </div>
        </section>
      </>
    )
  }
}
export default App;