import { useQuery } from '@tanstack/react-query'
// import { useHotkeys } from 'react-hotkeys-hook'
import { useState, useKeyDown } from 'react'

import {
  getCurrent,
  getNext,
  getPrevious,
  getFlip,
  getReset,
  getShuffle,
  getHide
} from './api'
import { MakeButton } from './MakeButton'

function Cards () {
  const [count, setCount] = useState(0)
  // useHotkeys('shift+=', () => setCount(count + 1), [count])
  // useHotkeys('shift+-', () => setCount(count - 1), [count])

  // useKeyDown(['Control', 'Enter'], () => {
  //   setCount(count + 1)
  // })

  const { isPending, error, data } = useQuery({
    queryFn: getCurrent,
    queryKey: ['cardData']
  })
  const [practiceInput, setPracticeInput] = useState('')
  // useHotkeys('meta+shift+k', () => setPracticeInput('reset'), [practiceInput])

  if (isPending) return 'Loading...'
  if (error) return 'An error has occurred: ' + error.message

  function handleKeyDown (e) {
    if (e.shiftKey && e.metaKey && e.key == 'k') {
      setPracticeInput('')
      setCount(count + 1)
    }
    if (e.ctrlKey && e.key == 'l') {
      setCount(0)
    }
  }

  return (
    <div>
      <div id='pile'>Pile: {data.pile}</div>
      <div id='number'>#{data.number}</div>
      <div id='order'>Order:{data.card_order.join(', ')}</div>
      <div id='front'>Side:{data.front ? 'Front' : 'Back'}</div>
      <div id='pile'>Counter: {count}</div>
      <div id='word'>{data.word}</div>
      <div id='sentence'>{data.sentence}</div>

      <form autoComplete='off'>
        <label autoComplete='new-password'>
          <input
            id='practiceSentenceIn'
            value={practiceInput}
            type='text'
            role='presentation'
            onChange={e => setPracticeInput(e.target.value)}
            onKeyDown={e => handleKeyDown(e)}
            autoComplete='off'
          />
        </label>
      </form>

      <div id='button_container'>
        <MakeButton mutationFn={getPrevious} text='Previous' />
        <MakeButton mutationFn={getNext} text='Next' />
        <MakeButton mutationFn={getFlip} text='Flip' />
        <MakeButton mutationFn={getShuffle} text='Shuffle' />
        <MakeButton mutationFn={getReset} text='Reset' />
        <MakeButton mutationFn={getHide} text='Hide' />
      </div>
    </div>
  )
}

export default Cards
