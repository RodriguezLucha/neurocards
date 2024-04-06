import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

import { getCurrent, getNext, getPrevious } from './api'

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

  if (isPending) return 'Loading...'
  if (error) return 'An error has occurred: ' + error.message

  return (
    <div>
      {data.number}
      {data.english_word}
      <button
        onClick={() => {
          previousMutation.mutate()
        }}
      >
        Previous
      </button>
      <button
        onClick={() => {
          nextMutation.mutate()
        }}
      >
        Next
      </button>
    </div>
  )
}

export default Cards
