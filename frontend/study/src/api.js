const getCurrent = async () => {
  const response = await fetch('/current')
  return response.json()
}
const getNext = async () => {
  const response = await fetch('/next')
  return response.json()
}
const getFlip = async () => {
  const response = await fetch('/flip')
  return response.json()
}
const getPrevious = async () => {
  const response = await fetch('/previous')
  return response.json()
}

export { getCurrent, getNext, getPrevious, getFlip }
