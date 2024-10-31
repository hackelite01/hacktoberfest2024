/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React, { useId } from 'react';

function InputBox({
	label,
	amount,
	onAmountChange,
	onCurrencyChange,
	currencyOptions = [],
	selectedCurrency = 'usd',
	amountDisabled = false,
	currencyDisabled = false,
	className = '',
}) {
	const inputId = useId();
	const selectId = useId();

	return (
		<div className={`bg-white p-3 rounded-lg text-sm flex ${className}`}>
			<div className='w-1-2'>
				<label htmlFor={inputId} className='text-black/80 mb-2 inline-block'>
					{label}
				</label>

				<input
					type='number'
					id={inputId}
					className='outline-none w-full bg-transparent py-1.5'
					placeholder='Amount'
					disabled={amountDisabled}
					value={amount ?? 0}
					onChange={(e) =>
						onAmountChange && onAmountChange(Number(e.target.value) || 0)
					}
				/>
			</div>

			<div className='w-1/2 flex flex-wrap justify-end text-right'>
				<p className='text-black/80 mb-2 w-full'>Currency Type</p>

				<select
					className='rounded-lg px-1 py-1 bg-gray-100 cursor-pointer outline-none'
					value={selectedCurrency}
					onChange={(e) => onCurrencyChange && onCurrencyChange(e.target.value)}
					disabled={currencyDisabled}
					id={selectId}
				>
					{currencyOptions.map((currency) => (
						<option key={currency} value={currency}>
							{currency}
						</option>
					))}
				</select>
			</div>
		</div>
	);
}

export default InputBox;
