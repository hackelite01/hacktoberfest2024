/* eslint-disable no-unused-vars */
import { useState } from 'react';
import useCurrencyInfo from './hooks/useCurrencyInfo.js';
import { InputBox, SwapButton } from './components/index.js';

function App() {
	const [from, setFrom] = useState('usd');
	const [to, setTo] = useState('inr');
	const [amount, setAmount] = useState(0);
	const [convertedAmount, setConvertedAmount] = useState(0);

	const currencyInfo = useCurrencyInfo(from);
	const options = Object.keys(currencyInfo);
	// console.log('Options: ', options);

	const imgUrl =
		'https://images.pexels.com/photos/14907339/pexels-photo-14907339.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1';

	const convertAmount = () => {
		setConvertedAmount((prevConvertedAmount) => {
			const newConvertedAmount = amount * currencyInfo[to];

			// console.log('Inside convertAmount(): ', amount, convertedAmount, from, to);

			return newConvertedAmount;
		});
	};

	return (
		<div
			className='w-full h-screen flex flex-wrap justify-center items-center bg-cover bg-no-repeat'
			style={{
				backgroundImage: `url(${imgUrl})`,
			}}
		>
			<div className='w-full'>
				<div className='w-full max-w-md mx-auto border border-gray-50 rounded-lg p-5 backdrop-blur-sm bg-white/30'>
					<form
						onSubmit={(e) => {
							e.preventDefault();
							convertAmount();
						}}
						name='inputForm'
					>
						<div className='w-full mb-1'>
							<InputBox
								label='from'
								selectedCurrency={from}
								amount={amount}
								currencyOptions={options}
								onCurrencyChange={(currency) => setFrom(currency)}
								onAmountChange={(amount) => setAmount(amount)}
							/>
						</div>

						{/* Swap Button */}
						{/* <div className='relative w-full h-0.5'>
							<SwapButton
								from={from}
								to={to}
								amount={amount}
								convertedAmount={convertedAmount}
								setFrom={setFrom}
								setTo={setTo}
								setAmount={setAmount}
								setConvertedAmount={setConvertedAmount}
							/>
						</div> */}

						<div className='w-full mb-1'>
							<InputBox
								label='to'
								selectedCurrency={to}
								amount={convertedAmount}
								currencyOptions={options}
								onCurrencyChange={(currency) => setTo(currency)}
								amountDisabled={true}
							/>
						</div>

						<button
							type='submit'
							className='w-full bg-blue-600 text-white px-4 py-3 rounded-lg mt-0.5'
						>
							Convert {from.toUpperCase()} to {to.toUpperCase()}
						</button>
					</form>
				</div>
			</div>
		</div>
	);
}

export default App;
