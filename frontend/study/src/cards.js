import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

import {
  getCurrent,
  getNext,
  getPrevious,
  getFlip,
  getReset,
  getShuffle,
  getHide
} from './api'

function Cards () {
  const queryClient = useQueryClient()

  const { isPending, error, data } = useQuery({
    queryFn: getCurrent,
    queryKey: ['cardData']
  })

  const previousMutation = useMutation({
    mutationFn: getPrevious,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })
  const nextMutation = useMutation({
    mutationFn: getNext,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })
  const flipMutation = useMutation({
    mutationFn: getFlip,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })
  const shuffleMutation = useMutation({
    mutationFn: getShuffle,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })
  const resetMutation = useMutation({
    mutationFn: getReset,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })
  const hideMutation = useMutation({
    mutationFn: getHide,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    }
  })

  if (isPending) return 'Loading...'
  if (error) return 'An error has occurred: ' + error.message

  return (
    <div>
      <div id='number'>#{data.number}</div>
      <div id='order'>Order:{data.card_order.join(', ')}</div>
      <div id='front'>Side:{data.front ? 'Front' : 'Back'}</div>
      <div id='word'>{data.word}</div>
      <div id='sentence'>{data.sentence}</div>

      <div>
        {makeButton(previousMutation, 'Previous')}
        {makeButton(nextMutation, 'Next')}
        {makeButton(flipMutation, 'Flip')}
        {makeButton(shuffleMutation, 'Shuffle')}
        {makeButton(resetMutation, 'Reset')}
        {makeButton(hideMutation, 'Hide')}
      </div>
    </div>
  )
}

export default Cards
function makeButton (nextMutation, buttonText) {
  return (
    <button
      onClick={() => {
        nextMutation.mutate()
      }}
    >
      {buttonText}
    </button>
  )
}
