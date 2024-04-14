const getCurrent = async () => {
  const response = await fetch('http://localhost:5003/current')
  return response.json()
}
const getReset = async () => {
  const response = await fetch('http://localhost:5003/reset')
  return response.json()
}
const getShuffle = async () => {
  const response = await fetch('http://localhost:5003/shuffle')
  return response.json()
}
const getNext = async () => {
  const response = await fetch('http://localhost:5003/next')
  return response.json()
}
const getFlip = async () => {
  const response = await fetch('http://localhost:5003/flip')
  return response.json()
}
const getPrevious = async () => {
  const response = await fetch('http://localhost:5003/previous')
  return response.json()
}
const getHide = async () => {
  const response = await fetch('http://localhost:5003/hide')
  return response.json()
}
const getPiles = async () => {
  const response = await fetch('http://localhost:5003/piles')
  return response.json()
}
const getCards = async () => {
  const response = await fetch('http://localhost:5003/cards')
  return response.json()
}
const getSwitch = async pile => {
  const response = await fetch(`http://localhost:5003/switch/${pile}`)
  return response.json()
}

export {
  getCurrent,
  getNext,
  getPrevious,
  getFlip,
  getCards,
  getReset,
  getShuffle,
  getHide,
  getPiles,
  getSwitch
}
