import { useMutation, useQueryClient } from '@tanstack/react-query'

export function MakeButton ({ mutationFn, text }) {
  const queryClient = useQueryClient()

  const mutation = useMutation({
    mutationFn: mutationFn,
    onSuccess: () => {
      queryClient
        .invalidateQueries({ queryKey: ['cardData'] })
        .then(queryClient.invalidateQueries({ queryKey: ['pileData'] }))
    }
  })

  return (
    <button
      onClick={() => {
        mutation.mutate()
      }}
    >
      {text}
    </button>
  )
}
