/*
ISSUE TO RESOLVE

Becasue of asynchronous nature of React state updates, the actual values may not reflect instantly after updation.
*/
/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import { useState } from 'react';

function SwapButton({
	from,
	to,
	amount,
	convertedAmount,
	setFrom,
	setTo,
	setAmount,
	setConvertedAmount,
}) {
	const [swapped, setSwapped] = useState(true);

	const swap = () => {
		const [newAmount, newConvertedAmount] = [convertedAmount, amount];
		const currFrom = from;
		const currTo = to;

		const swapAmount = () => {
			setAmount(() => newAmount);
			setConvertedAmount(() => newConvertedAmount);
		};

		const swapConvertedAmount = () => {};

		setFrom(currTo);
		setTo(currFrom);
		swapAmount();
		swapConvertedAmount();

		// console.log('Inside swap(): ', amount, convertedAmount, to, from);

		// setAmount((prevAmount) => {
		// 	setConvertedAmount((prevConvertedAmount) => {
		// 		setAmount(prevConvertedAmount);
		// 		return prevAmount;
		// 	});
		// 	return convertedAmount;
		// });

		// setFrom((prevFrom) => {
		// 	setTo(() => prevFrom);
		// 	return to;
		// });
	};

	return (
		<button
			className='absolute left-1/2 -translate-x-1/2 -translate-y-1/2 border-2 border-white rounded-md bg-blue-600 text-white px-2 py-0.5'
			onClick={() => {
				swap();
				setSwapped(false);
				return setSwapped(true);
			}}
		>
			Swap
		</button>
	);
}

export default SwapButton;
