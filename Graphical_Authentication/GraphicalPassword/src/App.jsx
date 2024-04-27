import React, { Component } from 'react'
import swal from 'sweetalert';
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
  componentDidMount = () =>{
    this.shuffleImages()
  }
  state = {
    images: {
      'computer': img1,
      'trailer': img2,
      'house': img3,
      'baby': img4,
      'plane': img5,
      'puppies': img6,
      'cat': img7,
      'bird': img8,
      'baby': img9
    },
    imagesValues:{
      firstImage:'',
      secondImage:'',
      thirdImage:''
    },
    username:''
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
    // for (let [key, value] of Object.entries(newImages)) {
    //   console.log(key, value);
    // }

  }
  handleSubmit  = (e)=>{
    e.preventDefault();
    if(!this.state.username){
      swal("Oops!", "You must fill in the username", "error")
      return;
    }
    //get the value of the images from their states
    const firstImage = document.querySelector('img#image-0').getAttribute('value');
    const secondImage = document.querySelector('img#image-1').getAttribute('value');
    const thirdImage = document.querySelector('img#image-2').getAttribute('value');
    if(firstImage===this.state.imagesValues.firstImage && secondImage===this.state.imagesValues.secondImage && thirdImage===this.state.imagesValues.thirdImage){
      swal(`Congratulations ${this.state.username}`, "You have succesfully passed Graphical Authentication", "success")
      //clear the fields
      this.setState({
        imagesValues:{
          firstImage:'',
          secondImage:'',
          thirdImage:''
        },
        username:''
      })
      this.shuffleImages()
    }else{
      swal("Oops!", "You have failed In matching one or more images. Please try again", "error")
    }
  }
  handleFormFieldChange = ({currentTarget:input}) => {
    let username = {...this.state.username}
    username = input.value
    this.setState({username})
  }
  handleChange = ({currentTarget:input})=>{
    const imagesValues = {...this.state.imagesValues}
    imagesValues[input.name] = input.value
    this.setState({imagesValues})
  }
  render = () => {
    return (
      <>
        <section className='w-[60%] h-screen m-auto font-serif text-xl flex flex-col justify-center items-center'>
          <h1 className='text-center font-serif text-3xl mt-2'>Graphical Authentication</h1>
          <div className="w-full">
            <form action="" className='w-[70%] m-auto text-sm shadow-xl p-2 bg-gray-200 flex flex-col gap-2 items-start' onSubmit={(e) => this.handleSubmit(e)}>
              <div className="form-group p-2">
                <label htmlFor="" className="label-control">Username</label>
                <input type="text" name="username" id="" className="form-control p-2" value={this.state.username}  onChange={this.handleFormFieldChange} />
              </div>
              <div className="graphical-password ">
                <div className="text-center">
                  Graphical Password
                </div>
                <div className="w-full">
                  <div className="flex flex-row justify-between items-center">
                    <div className="w-[50%] grid md:grid-cols-3 grid-rows-3 gap-0">
                      {Object.keys(this.state.images).map((image,index)=>(
                        index<=2 ? (
                          <div className="object-fit w-[90px] h-[60px]" key={index}>
                            <img src={this.state.images[image]} alt="" value={image} id={`image-${index}`} /> 
                          </div>
                        ):null
                      ))}
                    </div>
                    <div className="w-[50%] grid md:grid-cols-3 grid-rows-3 gap-3">
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 1</label>
                        <input type="text" className='w-20' name='firstImage' value={this.state.imagesValues.firstImage} onChange={this.handleChange}/>
                      </div>
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 2</label>
                        <input type="text" className='w-20' name='secondImage' value={this.state.imagesValues.secondImage}  onChange={this.handleChange}/>
                      </div>
                      <div className='w-full p-2'>
                        <label htmlFor="" className="label-control">Image 3</label>
                        <input type="text" className='w-20' name='thirdImage' value={this.state.imagesValues.thirdImage}  onChange={this.handleChange}/>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="flex flex-row justify-between items-center w-full gap-3">
                <button className='p-2 bg-orange-500 text-white text-bold w-[50%]' type='button' onClick={this.shuffleImages}>
                  Shufle Images
                </button>
                <button className=' w-[50%] p-2 bg-orange-500 text-white text-bold' type='submit'>
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