import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

import { getCurrent, getNext } from './api'

function Cards () {
  const queryClient = useQueryClient()

  const { isPending, error, data } = useQuery({
    queryFn: getCurrent,
    queryKey: ['cardData']
  })

  const mutation = useMutation({
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
          mutation.mutate()
        }}
      >
        Next
      </button>
    </div>
  )
}

export default Cards
