import { useQueries, useQueryClient } from '@tanstack/react-query'
// import { useHotkeys } from 'react-hotkeys-hook'
import { useState } from 'react'

import {
  getCurrent,
  getNext,
  getPrevious,
  getFlip,
  getReset,
  getShuffle,
  getHide,
  getPiles,
  getCards,
  getSwitch
} from './api'
import { MakeButton } from './MakeButton'

function Cards () {
  const queryClient = useQueryClient()

  const [count, setCount] = useState(0)
  // useHotkeys('shift+=', () => setCount(count + 1), [count])
  // useHotkeys('shift+-', () => setCount(count - 1), [count])

  // useKeyDown(['Control', 'Enter'], () => {
  //   setCount(count + 1)
  // })

  const results = useQueries({
    queries: [
      {
        queryFn: getCurrent,
        queryKey: ['cardData']
      },
      {
        queryFn: getPiles,
        queryKey: ['pileData']
      }
    ]
  })
  const { isPending, error, data } = results[0]
  const {
    isPending: isPendingPile,
    error: errorPile,
    data: dataPile
  } = results[1]

  const [practiceInput, setPracticeInput] = useState('')
  // useHotkeys('meta+shift+k', () => setPracticeInput('reset'), [practiceInput])

  if (isPending) return 'Loading...'
  if (error) return 'An error has occurred: ' + error.message
  if (isPendingPile) return 'Loading...'
  if (errorPile) return 'An error has occurred: ' + error.message

  function handleKeyDown (e) {
    if (e.shiftKey && e.metaKey && e.key === 'k') {
      setPracticeInput('')
      setCount(count + 1)
    }
    if (e.ctrlKey && e.key === 'l') {
      setCount(0)
    }
  }
  console.log(dataPile)

  return (
    <div>
      <label id='pick'>
        Pick a pile <nbsp></nbsp>
        <select
          name='selectedCard'
          defaultValue={data.pile}
          onChange={e => {
            switchPile(e)
          }}
        >
          {/* <option value='orange'>Orange</option> */}
          {dataPile.map(e => (
            <option>{e}</option>
          ))}
        </select>
      </label>

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

  function switchPile (e) {
    getSwitch(e.target.value).then(() =>
      queryClient.invalidateQueries({ queryKey: ['cardData'] })
    )
  }
}

export default Cards
