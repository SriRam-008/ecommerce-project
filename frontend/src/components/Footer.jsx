// export default function Footer() {
//   return (
//     <footer className="w-full py-4 border-t flex flex-col items-center text-sm text-gray-600 text-center">
//       <p className="flex flex-col items-center gap-1">
//         Developed with <span className="text-red-500">❤️</span> by{" "}
//         <a
//           href="https://www.linkedin.com/in/rathan-kumar492"
//           target="_blank"
//           className="text-blue-600 hover:underline"
//         >
//           Rathan Kumar
//         </a>
//       </p>

//       <div className="flex flex-col items-center gap-1 mt-2">
//         <a
//           href="mailto:developer.rathan@gmail.com"
//           className="text-blue-600 hover:underline"
//         >
//           developer.rathan@gmail.com{" "}
//         </a>

//         <span className="flex items-center gap-1 text-gray-500 text-sm">
//           <i className="bi bi-geo-alt-fill" style={{ fontSize: "20px" }}></i>
//           Mumbai, India
//         </span>
//       </div>
//     </footer>
//   );
// }





export default function Footer() {
  return (
    <footer className="w-full py-4 border-t flex flex-col items-center text-sm text-gray-600 text-center">
      <p className="flex flex-col items-center gap-1">
        Developed by{" "}
        <a
          href="https://www.linkedin.com/in/sriramr08/"
          target="_blank"
          className="text-blue-600 text-decoration-none"
        >
          Sri Ram R
        </a>
      </p>

      <div className="flex flex-col items-center gap-1 mt-2">
        <a
          href="mailto:contactsriramcse@gmail.com"
          className="text-blue-600 text-decoration-none"
        >
          contactsriramcse@gmail.com{" "}
        </a>

        <span className="flex items-center gap-1 text-gray-500 text-sm">
          <i className="bi bi-geo-alt-fill" style={{ fontSize: "20px" }}></i>
          Pondicherry, India
        </span>
      </div>
    </footer>
  );
}

