const getCurrent = async () => {
  const response = await fetch('/current')
  return response.json()
}
const getNext = async () => {
  const response = await fetch('/next')
  return response.json()
}

export { getCurrent, getNext }
