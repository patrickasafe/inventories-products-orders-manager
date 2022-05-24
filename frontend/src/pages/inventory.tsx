import type { NextPage } from 'next'
import Head from 'next/head'
import EnchancedTable from '../components/EnchancedTable'
import styles from '../styles/Home.module.css'



const Inventory: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <title>Inventory</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
        />
      </Head>
      <EnchancedTable>
        
      </EnchancedTable>
      
    </div>)
}
export default Inventory