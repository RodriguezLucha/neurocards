import { QueryClientProvider, QueryClient } from '@tanstack/react-query'

import Cards from './Cards'

function App () {
  const queryClient = new QueryClient()

  return (
    <QueryClientProvider client={queryClient}>
      <Cards />
    </QueryClientProvider>
  )
}

export default App
